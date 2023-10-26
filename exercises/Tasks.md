# Tasks

1. 在 interactive-app.py 文件中，添加一个 [radioItems Dash Core Component](https://dash.plotly.com/dash-core-components/radioitems) 至 layout 中，并添加三个 `options` 属性： `['blue','red','green']`。将 radioItems 组件添加进 callback 函数中，使它的结果更新 Markdown 文本的颜色。
- hint: To change the color of the Markdown text, set the `style` property like this: `dcc.Markdown(style={'color':'purple'})`

2. 在 app-with-graph.py 文件中，在 Markdown 文本和 Graph 之间添加一个空的  `Alert` [Dash Mantine Component](https://dash-mantine-components.herokuapp.com/components/alert)，将 `Alert` 的 `children` 属性作为第二个 `Output` 写入 callback 函数。返回值为字符串：
    - bar plot: "The data for the bar graph is highly confidential."
    - scatter plot: "The scatter plot is believed to have been first published in 1833"

3. 在 app-with-graph.py 文件中重新定义布局，使下拉菜单和 choropleth 图彼此相邻，在同一行中。 一行内的列的总宽度必须等于或小于 12。
- hint: 参考 [Dash Bootstrap docs](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/) 中的例子

4. 在 3 的代码的基础上，将 choropleth 图改为 bar chart 柱状图。柱状图的 x 轴代表 'STATE'，y 轴代表下拉列表中的 "column_name"。
- hint: 参考 [the bar chart](https://plotly.com/python/bar-charts/).

5. 在 4 的码的基础上，将 bar chart 柱状图改成 line chart 条形图。 x 轴代表年份，y 轴代表“column_name”，颜色代表州。
- hint: 参考 [the line chart](https://plotly.com/python/line-charts/).