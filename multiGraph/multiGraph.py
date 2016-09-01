'''
display multiple charts via Bokeh (not Flask)
source: http://bokeh.pydata.org/en/0.10.0/docs/user_guide/layout.html
'''
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from flask import Flask, render_template
from bokeh.io import gridplot, output_file, show
from bokeh.charts import Line, output_file, show

app=Flask(__name__)

@app.route('/simpleline.html')
def simpleLine():
	x = list(range(11))
	y0 = x
	y1 = [10-i for i in x]
	y2 = [abs(i-5) for i in x]

	# create a new plot
	s1 = figure(width=500, plot_height=500, title=None)
	s1.circle(x, y0, size=10, color="navy", alpha=0.5)

	# create another one
	s2 = figure(width=500, height=500, title=None)
	s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

	# create and another
	s3 = figure(width=500, height=500, title=None)
	s3.square(x, y2, size=10, color="olive", alpha=0.5)

	# create and another
	s4 = figure(width=500, height=500, title=None)
	s4.line(x, y2, size=10, color="olive", line_width=2)
	# p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

	# put all the plots in a grid layout
	p = gridplot([[s1, s2], [s3, s4]])
	script,div=components(p)
	return render_template('simpleline.html',div=div,script=script) #this line matters!
	output_file("simpleline.html")
	show(p)



@app.route('/simplecirc.html')
def simpleCirc():
    fig2=figure(title="Sensor data")
    fig2.line([1,2,3,4],[2,4,6,8])
    # global script
    # global div
    script,div=components(fig2)
    return render_template('simplecirc.html',div=div,script=script) #this line matters!
    output_file("simplecirc.html")
    show(fig)
# fig=figure(title="Sensor data")
# fig.line([1,2,3,4],[2,4,6,8])
# script,div=components(fig)

# @app.route('/simplecirc.html')
# def simpleLine():
#     fig=figure(title="Sensor data")
#     fig.line([1,2,3,4],[2,4,6,8])
#     global script
#     global div
#     script,div=components(fig)
#     return render_template('simplecirc.html',div=div,script=script) #this line matters!
#     output_file("simpleline.html")
#     show(fig)

# fig=figure(title="Sensor data")
# fig.line([1,2,3,4],[2,4,6,8])
# script,div=components(fig)


if __name__ == "__main__":
    app.run(debug=True,port=5002)