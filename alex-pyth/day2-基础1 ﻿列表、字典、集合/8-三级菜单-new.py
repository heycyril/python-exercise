menu = {

    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{"oldboy","test.yaml"},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{"链家地产","我爱我家"},
        },
        '朝阳':{
            "望京":["奔驰","陌陌"],
            "国贸": ["CICC","HP"],
            "东直门": ["Advent","飞信"],
        },
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{'32':'21'},
    },
    '山东':{},
}
exit_flag = False
current_layer = menu

layers = [menu]

while not  exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        #print("change to laster", current_layer)
        layers.pop()
    elif choice not  in current_layer:
        continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]


