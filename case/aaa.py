import jsonpath
import json
# from common.MyExcel_ import ExcelUtil
from openpyxl import Workbook,load_workbook


json1={ "store": {
           "book": [
              { "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
              },
              { "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
              },
              { "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
              },
              { "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
              }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
aaa=jsonpath.jsonpath(json1,"$.store.book[0].price")
bbb=(1,"aaaw\n","ww\n",None)
ddd=(2,"dddw\n","ww\n",None)
ccc=[bbb,ddd]
# print(str(bbb))
# print(str(ccc))
# ll = [str(x).strip() for x in ccc if str(x).strip()!= '']


print(pan(ccc))








