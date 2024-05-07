# Formatting settings for VSCode
1. install Black Formatter extension by Microsoft from VSCode extentions marketplace
2. in VSCode settings, add these 2 lines 
``` json
"python.formatting.provider": "black",
"python.formatting.blackArgs": ["--line-length", "120"],
```