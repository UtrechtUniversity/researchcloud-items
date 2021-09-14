# How to create icons for SURF ResearchCloud plugins
[back to index](index.md)

Assuming that you have a file `icon.png`. This image can be
encoded as a text file base64 using the following bash command:
```
echo "data:image/png;base64,$(base64 -w 0 icon.png)" >icon.txt
```

