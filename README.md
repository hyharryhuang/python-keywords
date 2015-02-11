# python-keywords
Outputs keywords from a string (without stopwords/URLs/mentions/RTs).

##Usage

If you're getting rid of stopwords, install nltk: `pip install -r /path/to/requirements.txt`.

```python
import python_keywords as pk

print(pk.removeLinksFromString("http://www.google.com hello")); //returns "hello"
```
