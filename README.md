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

## Duration utility

`duration_utils.to_minutes(seconds)` converts a non-negative integer number of
seconds to whole minutes, rounding up when there are leftover seconds. For
example, `to_minutes(0)` returns `0`, `to_minutes(59)` returns `1`, and
`to_minutes(61)` returns `2`. Booleans and other non-integer inputs raise
`TypeError`; negative integers raise `ValueError`.

```python
from duration_utils import to_minutes

print(to_minutes(61))  # 2
```

Run the tests with `python -B -m unittest -v`.
