Title: The great directory egg hunt (HSCTF 9) <br>
Desc: Lots of branching paths, but how do we get to the correct file? <br>
Target: https://hsctf-9-resources.storage.googleapis.com/uploads/c93000e33ecfa719657c78f57ce7b18ac2467ff73d3a8d1f820c0f241764cca2/dir.zip (dir.zip)

Using 'tree' command on Windows/Linux, I can list down all the folders and files inside the directory. Here I have a massive amount of folders and files, up to 8k folder and 4k files.

![image](https://user-images.githubusercontent.com/63649797/173051889-dcfbbc73-6fb9-44aa-b050-0e357a984b79.png)
and so on.. <br><br>

All of the endings of this folder will go to a 'file.txt'. Most of them will contain "Nope" and its size is only 4 byte. <br>
![image](https://user-images.githubusercontent.com/63649797/173052463-51b3ad07-df68-4d65-b51f-149c1556d2d5.png)
<br>

Using a correct command of find in the terminal, I am able to filter the findings based on file size. <br>
In this case, I am are using: ``find . -type f -size 4c``
![image](https://user-images.githubusercontent.com/63649797/173052952-f41120af-5580-43df-ab0c-514dbf02dbb4.png)
<br>
Explanation: <br>
 -type f : is to filter regular file <br>
 -size +4c : plus sign indicates 'more than or exactly' of 4 bytes

Hence, I can get the file appropriate with the filter and its location.
![image](https://user-images.githubusercontent.com/63649797/173053749-e4d1bf2d-fcf4-474f-940f-5c8308dd4109.png)
<br><br>

Flag
```
flag{Tw3lv3_D1rs_D33p_6GiTQEz}
```
