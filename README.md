**Emotional Data Data Visualisation**

The brief was to visualise the anonymous emotional csv data and be creative, snip of original data directly below.

![image](https://user-images.githubusercontent.com/76686112/124918007-6b46a580-dfec-11eb-98e5-00e9521c9dbb.png)

The data was manipulated and visualised using Python, see technical assessment below.

**Initial Analyses and Charts**

Through eye balling data it was noted that positive emotions tended to -1 on the x axis.  There was not a clear correlation between y value and type of emotion; however it was thought perhaps it related to feeling introspective and extrospective which would affect whether the sympathetic or the parasympathetic nervous system were being used by the body.

Initial analysis of data plotting bubble chart: the centre of the circles represent the x and y co-ordinates of each emotion and the area of the circle relating to the frequency of that emotion.  It is hard to draw conclusions from the figure. However, the larger circles (emotions that occurred most frequently) generally are located in the negative x side of the figure and therefore are generally more positive emotions than negative. 


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2Foi-yA8FlCB.png?alt=media&token=b8814475-0aba-48b4-9edd-5e2029bffac4)


The first graph that told a story: A bar chart showing x co-ordinates against frequency of the emotions.  The outlier is clearly the central bar with a frequency of more than 160.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2FHiDiKxG27N.png?alt=media&token=f3beeac7-b384-42b3-894c-90ae646f68e0)

 
Outliers: The great majority occurred one time.  Therefore, removing the outliers from a frequency point of view using IQR would remove the emotions that occurred the most and would not represent the data correctly.  Outliers were not removed on this basis; and also considering it is a reasonably small dataset.

[See function: remove_outliers_inter_quantile_range]

To obtain better conclusions from the bubble chart; the data was converted to mean co-ordinates; and sorted in terms of frequency. This was shown on a bubble chart with each bubble representing the group of emotions the occurred a certain frequency:

*	where the centre of the circles represent the mean x and y; and 
*	the area of the circles represent the number of emotions that occurred

The graph contains less noise and infers more of a trend than the original scatter plot; the frequency groups comprising a larger number of emotions; (their mean co-ordinates) are located centrally both in the x and y axes.  This is discussed further in the section below.


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2Femz9sME2fo.png?alt=media&token=c63fab3e-85a2-4ff9-9dcd-b310085721ac)


**Final Charts**

(i)	Bubble Chart
The second bubble chart was then colour coded in line with the occurrence of emotions.  The colour bar below was intended to appear in the figure, it shows the occurrence of the emotions (i.e. log_count):


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2Fm9SLwjRV2P.png?alt=media&token=3e399f63-d7f1-434f-ad79-e8ce0d40e3de)


The figure is below which uses the x and y mean values for the circle centres; and the size of the circles are governed by the number of emotions with the particular log_count:

Please note for visualisation of the bubbles, the size scale is multiplied by 10.  The figure shows clearly that the larger circles (groups with larger number of emotions) are groups where the emotions occurred very few times.

See figure further below for 1:1 scale for size.

Conclusions: The largest circles are generally central; however pale in colour. The darkest circles are very small and are not generally central, they are located in the negative x; and therefore appear to be positive emotions.  There are very few points that are located in the positive x; therfore the mean appear to be positive emotions.  There is one outlier for a single emotion that is very close to the max positive x which would suggest a very negative emotion.  This single outlier shows how the emotions trend positive/neutral.


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2Flv_ArSzLwx.png?alt=media&token=1a050362-8be5-40b1-9d0f-333f742cec46)


![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2FWphC9olKmk.png?alt=media&token=ec3888e0-ccfc-49ff-8fa8-6f6c90fa40be)


 
Figure below included for reference.  Note the scale for number of emotions vs size of bubble is 1:1.  
 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2FQ1K5985NgY.png?alt=media&token=b2991a74-85a7-47b8-be0e-c650941fe811)



(ii)	Bar Chart
The histogram was overlayed with y co-ordinates for the emotions.  Conclusions:

*	The more positive emotions are towards the negative x; where there is an frequency between x and y co-ordinates.  
*	Where there is extreme frequency in one co-ordinate axis; there is little frequency from the other
*	the negative emotions show a high frequency in y without much frequency in x
 
 
 ![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FIanshaw93%2FjeIPQhJm-F.png?alt=media&token=205c6cac-d6e0-41cb-9ad6-596400d4b400)
 
 
**Further Work and things I would change**

*	The aim for the histograms was to have the x and y bars stacked on top of each other.
*	The colour scheme for the final bubble chart would ideally be in a colour map without white; the colour bar would be located on the figure and the legend for the size scale would match the number of emotions.
*	Greater study of the mean x and y co-ordinates to infer further trends.

**Things I learned**

*	Map function (mapping key of dictionary to column of dataframe - function: manipulate_dataframe)
*	List comprehension (shorter syntax for creating a list from an exisitng list - see function: scatter_plot2)
*	Bubble charts
*	Colour maps
*	Charting legends
*	How to perform IQR using python
