from transformers import AutoTokenizer, AutoModelForCausalLM

CHECKPOINT_DIR = "./run125/checkpoints/latest-rank0.pt"

model = AutoModelForCausalLM.from_pretrained(CHECKPOINT_DIR)
import code
code.interact(local=locals())