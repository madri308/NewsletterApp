# NewsletterApp

This is a mac application useful to send html newsletters via outlook.

## Features:

- Preset recipients data.
- Load or paste HTML code.
- Merge styles linked to the html automatically.
- Open/Send the mail with outlook.
- Visualize the mail with a browser.
- Load a signature, for this you should create a signature with no images called "StandardNoImages".

## How to run it:

Clone the repo

### Manually

Install the reqs

```
pip install -r requirements.txt
```

Run the next command in the project root folder

```
python3 NewsletterApp.py
```

### Application

Run ```NewsletterApp.app```

If the app is not sending/opening the mail, go to System Settings -> Privacy & Security and check the Automation section

## Tech details

### Recipients data format

```
[
  {
    "name": "For Testing",
    "to_recipient": "xxx@gmail.com, yyy@gmail.com",
    "cc_recipient": "mmm@gmail.com"
  },
  {
    "name": "Nice newsletter",
    "to_recipient": "group1@company.com, group2@company.com",
    "cc_recipient": "boss@company.com,
  }
]
```

### How the app access Outlook without credentixals

We use a library called appscript, you can check the things you can do with it by opening the Script Editor -> File -> Open Dictionary and selecting any application