# CS50 Python Course Setup

## CS50 MIT GitHub Repository

- https://submit.cs50.io/courses
- https://submit.cs50.io/users/pingv

## Testing and Submission Commands

### Check if tools are installed
```bash
check50 --version
submit50 --version

```

### Install required tools
```bash
pip install check50
pip install submit50
```

### Update tools
```bash
pip3 install -U cs50
pip3 install -U submit50
```

### Check if tools are updated
```bash
check50 --version
submit50 --version
```

##### Einstein
```bash
# Test your code
check50 cs50/problems/2022/python/einstein

# Submit your solution
submit50 cs50/problems/2022/python/einstein
```

### Notes

Run commands from the specific problem directory
GitHub authentication is required for submission

```bash
#Example
(.venv) vishnuparandhaman@Vishnus-MacBook-Air-2 indoor % pwd
$ /Users/vishnuparandhaman/code/python2024/cs50-py-dmalon/week0/indoor

# Note that except for the last directory (here, indoor) the path is different
# --- cs50/problems/2022/python/indoor
# --- /Users/vishnuparandhaman/code/python2024/cs50-py-dmalon/week0/indoor
(.venv) vishnuparandhaman@Vishnus-MacBook-Air-2 indoor % check50 cs50/problems/2022/python/indoor
Connecting.....
```
