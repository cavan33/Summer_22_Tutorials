# Hugging Face Text Classification Lesson
# https://huggingface.co/docs/transformers/tasks/sequence_classification

# (https://huggingface.co/docs/datasets/installation)
from datasets import load_dataset
imdb = load_dataset("imdb")
# Then take a look at an example:
imdb["test"][0]
# ^ Contains "text" (review) and a "label" (0 or 1 for positive or negative)

# Load the DistilBERT tokenizer to process the text field:
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


# Create a preprocessing function to tokenize text and truncate sequences to be no longer than DistilBERT’s maximum input length:
def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

# Use datasets map function to apply the preprocessing function over the entire dataset:
tokenized_imdb = imdb.map(preprocess_function, batched=True)

# View:
tokenized_imdb["test"][0]

# Note: I used PyTorch syntax, not TensorFlow syntax, on the upcoming parts.
# Create a batch of examples:
from transformers import DataCollatorWithPadding
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Train:
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=5,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_imdb["train"][1:100],
    eval_dataset=tokenized_imdb["test"][1:100],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()