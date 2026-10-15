## Hi there 👋

--
**ifox777/ifox777** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

### Compress integer ranges

`range_utils.compress_ranges` sorts and deduplicates a list of integers, then
returns inclusive ranges for consecutive values:

```python
from range_utils import compress_ranges

print(compress_ranges([5, 1, 2, 2, 4, 9]))  # [(1, 2), (4, 5), (9, 9)]
```

Run the tests with `python -B -m unittest -v`.
