from transformers import AutoTokenizer, GPT2Config, AutoModelForCausalLM
from transformers import AutoConfig

config = AutoConfig.from_pretrained('EleutherAI/gpt-neo-125m')

# CHECKPOINT_DIR = "./run125/checkpoints/latest-rank0.pt"

model = AutoModelForCausalLM.from_pretrained('./run125/checkpoints/latest-rank0.pt', config=config)


from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForCausalLM

model = ORTModelForCausalLM.from_pretrained("./run125/", config=config, from_transformers=True)
tokenizer = AutoTokenizer.from_pretrained("gpt2")

import code
code.interact(local=locals())
