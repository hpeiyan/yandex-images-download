# Yandex Images Download
Python Script to download images from Yandex.Images.

# Features
* Checking for captcha presence
* Many filters
* Multiproccessing is available (option `--num-workers`)

# Main requirements
* Python 3.7+
* [Selenium Wire](https://github.com/wkeeling/selenium-wire) 1.0.8+
* Firefox, Chrome, Safari and Edge are supported

# Installation
1. Get [Selenium driver executable](https://www.seleniumhq.org/about/platforms.jsp) for your browser and platform. Firefox, Chrome, Safari and Edge are supported.  
Use option `--driver-path` to specify the driver's path or add the executable in your PATH.


# Examples
Simple example using [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/):

```$ yandex-images-download Chrome --keywords "vodka, bears, balalaika" --limit 10```

Example of using keywords from input file with specific image extension/format:

```$ yandex-images-download Chrome --keywords_from_file input_example.txt --itype=png```

All other information can be obtained with the `--help` argument.


# Acknowledgements
Special thanks to Andrey Lyashko for code reviews.  
Special thanks to Boris Kovarski (https://github.com/kovarsky) and Andrey Lyashko for backing the project.

# Another features:
1. Search alike image with similar function:
```bash
➜  ~ yandex-images-download Chrome --driver-path ~/chromedriver --limit 8 --output-directory ~/Desktop --keywords "https://www.xxx.jpg" --similar-images True
```

2. Point to the domain of the Yandex Image Search
```bash
➜  ~ yandex-images-download Chrome --driver-path [chromedriver_path] --yandex-country [you_select_country]

```

3. Fix the bug about the Filter of Image Search
```bash
--isize {large,medium,small}
                        image size
--exact-isize EXACT_ISIZE EXACT_ISIZE
                        exact image resolution
--iorient {horizontal,vertical,square}
                        orient of image
--type {photo,clipart,lineart,face,demotivator}
                        image type
--icolor {color,gray,red,orange,cyan,yellow,green,blue,violet,white,black}
                        filter on color
--itype {jpg,png,gifan}
```

# Whole Features:
```bash
1.➜  yandex-images-download git:(master) ✗ yandex-images-download --help
2.usage: yandex-images-download 
3.arguments:
4.  -h, --help            show this help message and exit
5.  -dp DRIVER_PATH, --driver-path DRIVER_PATH
6.                        path to brower's WebDriver
7.  -k KEYWORDS, --keywords KEYWORDS
8.                        delimited list input, separated by a comma
9.  -kf KEYWORDS_FROM_FILE, --keywords-from-file KEYWORDS_FROM_FILE
10.                        extract list of keywords from a text file. one line =
11.                        one keyword.
12.  -q, --quiet-mode      do not logging.info() messages
13.  -x SINGLE_IMAGE, --single-image SINGLE_IMAGE
14.                        downloading a single image from URL
15.  -o OUTPUT_DIRECTORY, --output-directory OUTPUT_DIRECTORY
16.                        download images in a specific main directory
17.  -l LIMIT, --limit LIMIT
18.                        delimited list input. default: 100
19.  --isize {large,medium,small}
20.                        image size
21.  --exact-isize EXACT_ISIZE EXACT_ISIZE
22.                        exact image resolution
23.  --iorient {horizontal,vertical,square}
24.                        orient of image
25.  --type {photo,clipart,lineart,face,demotivator}
26.                        image type
27.  --icolor {color,gray,red,orange,cyan,yellow,green,blue,violet,white,black}
28.                        filter on color
29.  --itype {jpg,png,gifan}
30.                        image extension type
31.  --commercial {1}      add commerce check
32.  --recent {7D}         add recency check
33.  --json JSON           save results information to json file
34.  --num-workers NUM_WORKERS
35.                        number of workers
36.  -s SIMILAR_IMAGES, --similar-images SIMILAR_IMAGES
37.                        search similar images by urls instead of keywords
38.  -y {com,ru,ua,by,kz,uz,tr}, --yandex-country {com,ru,ua,by,kz,uz,tr}
39.                        destinatate the target of Yandex Image Domain to craw
```
