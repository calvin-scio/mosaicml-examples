from transformers import AutoTokenizer, GPT2Model

CHECKPOINT_DIR = "./run125/checkpoints/latest-rank0.pt"

model = GPT2Model.from_pretrained(CHECKPOINT_DIR)
import code
code.interact(local=locals())
