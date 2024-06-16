# Formatting settings for VSCode
1. install Black Formatter extension by Microsoft from VSCode extentions marketplace
2. in VSCode settings, add these 2 lines 
``` json
"python.formatting.provider": "black",
"python.formatting.blackArgs": ["--line-length", "120"],
```
&nbsp;
# Commit messages
| Commit Type | Title |Description |
|:------------|:------|:------------|
feat	| Features| 	A new feature	
fix	    | Bug  Fixes|	A bug Fix	
docs	| Documentation|	Documentation only changes	
style	| Styles|	Changes that do not affect the meaning of the   code (white-space, formatting, missing semi-colons, etc)	
refactor|	Code Refactoring|	A code change that neither fixes a bug nor adds a feature	
perf	|Performance Improvements|	A code change that improves performance	
test	|Tests|	Adding missing tests or correcting existing tests
build	|Builds|	Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)	
ci	|Continuous Integrations|	Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)	
chore	|Chores|	Other changes that don't modify src or test files	
revert	|Reverts|	Reverts a previous commit

source: https://github.com/pvdlg/conventional-commit-types/blob/master/README.md

## Message format
```
git commit -m "[Commit Type]: [Desctription]"
```

### Example
```
git commit -m "docs: update README file"
```