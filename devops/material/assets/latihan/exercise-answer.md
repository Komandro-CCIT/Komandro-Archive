
# Exercise 1

```bash
#!/bin/bash

# Move to home
cd ~

# Clone repo
git clone https://github.com/Komandro-CCIT/devops-exercise.git

# Move to Exercise-1
cd devops-exercise/exercise-1

# Create new folder based on extensions
mkdir static media code

# Move all .js and .css
mv *.js *.css code/

# Move all .png
mv *.png static/

# Move rest of the file to static
mv *.gif *.mp3 media/

# List all moved file 
cd /home/ubuntu/devops-exercise/exercise-1
ls -R
```

# Exercise 2


```bash
# Move to exercise1
cd /home/ubuntu/devops-exercise/exercise-1
```

```bash
# Creating global variable timestamp
TIMESTAMP=$(date +"%Y-%m-%d_%H:%M:%S")
```

```bash
# Creating back up
tar -cvzf ../exercise-2/target-a/$TIMESTAMP.tar.gz code/
TIMESTAMP=$(date +"%Y-%m-%d_%H:%M:%S")
tar -cvzf ../exercise-2/target-b/$TIMESTAMP.tar.gz media/
TIMESTAMP=$(date +"%Y-%m-%d_%H:%M:%S")
tar -cvzf ../exercise-2/target-c/$TIMESTAMP.tar.gz static/
```

```bash
# Delete all backup 
rm -rf ../exercise-2/target-{a,b,c}/*
```

`backup.sh`:

```bash
#!/bin/bash

# Move to exercise1
cd /home/ubuntu/devops-exercise/exercise-1

# Creating back up
for target in a b c; do
  case $target in
    a) folder="code";;
    b) folder="media";;
    c) folder="static";;
  esac
  sleep 2
  TIMESTAMP=$(date +"%Y-%m-%d_%H:%M:%S")
  tar -cvzf ../exercise-2/target-$target/$TIMESTAMP.tar.gz $folder/
done

echo "Backup Success!"
```
