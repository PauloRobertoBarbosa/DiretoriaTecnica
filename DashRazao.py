# import cufflinks as cf
# from plotly.offline import iplot
# import pandas as pd
# import numpy as np
# import plotly
#
# df = pd.DataFrame(np.random.randn(100,4), columns=['A','B','C','D'])
# cf.go_offline()
# iplot(df)

import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'jpg'

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()