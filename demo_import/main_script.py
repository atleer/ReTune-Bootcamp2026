# %%
import sys
sys.path.insert(0, 'demo_import/src')

from utils import add_numbers
from process import subtract_numbers

# %%
a = 5
b = 9

c = add_numbers(a, b)

print(f"c = {c}")
# %%

subtract_numbers(b, a)
