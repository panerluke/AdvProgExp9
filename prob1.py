import pandas as pd

bearsdct1 = {
        'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Math': [80, 90, 79]
        }

bearsdct2 = {
        'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Electronics': [85, 81, 83]
        }

bearsdct3 = {
        'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'GEAS': [90, 79, 93]
        }

bearsdct4 = {
        'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'ESAT': [93, 89, 88]
        }

bears1 = pd.DataFrame(bearsdct1, columns = ['Student', 'Math'])
bears2 = pd.DataFrame(bearsdct2, columns = ['Student', 'Electronics'])
bears3 = pd.DataFrame(bearsdct3, columns = ['Student', 'GEAS'])
bears4 = pd.DataFrame(bearsdct4, columns = ['Student', 'ESAT'])

bears5 = pd.merge(bears1, bears2)
bears6 = pd.merge(bears5, bears3)
bears = pd.merge(bears6, bears4)