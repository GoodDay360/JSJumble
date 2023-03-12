# JSJumble
**Tool for obfuscating, compressing Javascript, and collecting static files.**  

# Installation
```
pip install pygesture
```

# Getting Started
- First import `JSJumble` to your script.


- **[ Required ]** Directory that you want to start converting.
```python
import JSJumble

JSJumble.static_dir = "./static"
```

- **[ Required ]** Directory to save converted static.
```python
JSJumble.converted_dir = "./converted"
```

- **[ Optional ]** Specify where to save cache file. `Default: Current Working Directory`
```python
JSJumble.cache_dir = "./cache.sql"
```

- **[ Optional ]** IP that engine will run on. `Default: "127.0.0.1"`
```python
JSJumble.host = "127.0.0.1"
```

- **[ Optional ]** Port that engine will run on. `Default: 80`
```python
JSJumble.port = 80
```

- **[ Optional ]** Should engine copy only javascript files only or not. `Default: False`
```python
JSJumble.js_only = False
```


- **[ Optional ]** Should engine delete files inside converted directory that are not listed inside static directory. `Default: True`
```python
JSJumble.delete_unlisted = True
```

- **[ Optional ]** Engine options that required to start converting. `Default: Listed below`
- You can find more additional options in this [Github Repo](https://github.com/javascript-obfuscator/javascript-obfuscator#javascript-obfuscator-options)
```python
JSJumble.engine = {
    "compact": True,
    "controlFlowFlattening": False,
    "deadCodeInjection": False,
    "debugProtection": False,
    "debugProtectionInterval": 0,
    "disableConsoleOutput": True,
    "identifierNamesGenerator": "hexadecimal",
    "log": False,
    "numbersToExpressions": False,
    "renameGlobals": False,
    "selfDefending": True,
    "simplify": True,
    "splitStrings": False,
    "stringArray": True,
    "stringArrayCallsTransform": False,
    "stringArrayEncoding": [],
    "stringArrayIndexShift": True,
    "stringArrayRotate": True,
    "stringArrayShuffle": True,
    "stringArrayWrappersCount": 1,
    "stringArrayWrappersChainedCalls": True,
    "stringArrayWrappersParametersMaxCount": 2,
    "stringArrayWrappersType": "variable",
    "stringArrayThreshold": 0.75,
    "unicodeEscapeSequence": False
}

```