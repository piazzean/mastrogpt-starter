import os, requests as req
import vision
import bucket
import uuid
import base64

USAGE = "Please upload a picture and I will tell you what I see"
FORM = [
  {
    "label": "any pics?",
    "name": "pic",
    "required": "true",
    "type": "file"
  },
]

def form(args):
  res = {}
  out = USAGE
  inp = args.get("input", "")
  buc = bucket.Bucket(args)

  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
    print(f"uploaded size {len(img)}")
    imgDecoded = base64.b64decode(img)
    # print(f"imgDecoded: {imgDecoded}")
    s3res = buc.write("andrea", imgDecoded)
    if s3res != "OK":
      out = f"Errore Salvataggio su S3: {s3res}"
    else:
      vis = vision.Vision(args)
      out = vis.decode(img)
      res['html'] = f'<img src="data:image/png;base64,{img}">'
    
  res['form'] = FORM
  res['output'] = out
  return res
