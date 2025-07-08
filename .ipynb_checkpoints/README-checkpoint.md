# Assignment 3 README
## Purpose
The purpose of assignment 3 was to first learn how to make a branch in github and add the MSE with more annotations onto the plot itself. I then printed the plot and statistics and using markdown notes for each segment of code.

## Methods to create the scatter plot and regression line
I created a scatter plot with two variables from our regression_data.csv dataset that was read using pandas to read the data and matplotlib in python. I then used numpy to convert the files and setting x and y. "Dataset" and "model" was used in R to make the scatter plot and fit a linear model. I then fit a linear regression model and plotted the regression line. This was done in Python by using plt.plot. In R, I used ggplot2 to overlay the regression line. In Python, you use color="blue" to make the color, but in R you use colour = 'red'. For x and y labels on Python you use plt.xlabel(""), but on R you use xlab(''). 
 

## Methods to create the intercepts, p value, standard error, equation and MSE
After fitting the plot and performing linear regression to get line of best fit, I added the the intercepts from the data file, the p value which can be used to test the significance of the data, standard error, and then the equation for the plot, which is based on the scatter data. 
### This was done in python with: 
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept 
### And this in R: 
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(data[[x_col]], data[[y_col]])
pred <- predict(model) in R. 
### These points were added directly to the plot using this in python:
plt.text(
    1,                   
    max(y) - 3500,            
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"r = {r_value:.2f}\n"
    f"MSE = {mse:.2f}",
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.5)  
)
### And added this with R: 
equation_text <- paste0(
  "Equation: y = ", round(slope, 2), "x + ", round(intercept, 2), "\n",
  "Correlation (r): ", round(r, 2), "\n",
  "MSE: ", round(mse, 2)
)

The last portion that I added for assignment 3 calculates mean squared error between the predictions and the actual values.
### In python:
mse = mean_squared_error(y, y_pred)

### In R:
mse <- mean((data[[y_col]] - pred)^2)

In addition to adding these on the plot directly, I also used print() in python and cat() in R to print in the terminal. I then saved it as a png and then printed the plots.


## What is MSE?
Mean squared error quantifies how close the model predicts the actual data.It emphasizes large errors more than smaller ones due to squaring.The formula for MSE is MSE = (1/n)*Σ (yᵢ - ŷᵢ)² and the units are squared units of y. The smaller the MSE, the better fit the model is.

## Interpretation of results
The equation for the plot is 8285.29x + 29203.52. This shows a positive correlation with YearsExperience and Salary. The r value is 0.89. The MSE was 17523844.08, which is a large MSE, meaning that the model is not fit very well. This is probably becuase there are only a few data points and they are scattered around the line, but not very close. 
