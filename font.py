import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib as mpl

fm.fontManager.addfont("/Library/Fonts/Montserrat-Regular.ttf")
mpl.rcParams['font.family'] = 'Montserrat'

fonts = [f.name for f in fm.fontManager.ttflist]
print("Montserrat" in fonts)

