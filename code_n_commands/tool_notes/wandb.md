
# Basic definitions

1. Entity: the team name, eg: `leomqyu-the-university-of-hong-kong`
2. Project: just a project, might have many runs
3. Run: a "training", eg with name `swift-breeze`, or `0108201611_ef_mine_22_corrstride`


# A typical wandb setup in python code

```python
import random
import wandb

# Start a new wandb run to track this script.
run = wandb.init(
    # Set the wandb entity where your project will be logged (generally your team name).
    entity="leomqyu-the-university-of-hong-kong",
    # Set the wandb project where this run will be logged.
    project="my-awesome-project",
    # Track hyperparameters and run metadata.
    config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    },
)

# Simulate training.
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2**-epoch - random.random() / epoch - offset
    loss = 2**-epoch + random.random() / epoch + offset

    # Log metrics to wandb.
    run.log({"acc": acc, "loss": loss})

# Finish the run and upload any remaining data.
run.finish()
```

# Sync local to online

`wandb sync proj_dir/wandb/offline-run-20260108_162402-0zhbs625`

Note: some times (eg on a shared server) might sync to other people's wandb account, if not sure, can add `-e <entity_id>`