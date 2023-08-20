## Section 03: Predictive Models

#### Table of Contents
- Linear Regression
- Polynomial Regression
- Multiple Regression, and Predicting Car Prices
- Multi-Level Models



### Linear Regression

#### Linear Regression
- Fit a line to a data set of observations
- Use this line to predict unobserved values


#### Linear Regerssion: How does it work?
- Usually using "least squares"
- Minimizes the squared-error between each point and the line
- Remember the slope-intercept equation of a line: `y = mx + b`
- The slop is the correlation between the two variables times the standard
  deviation in Y, all divided by the standard deviation in X.
- The intercept is the mean of Y minus the slope times the mean of X
- Python will do all that for you.
- Least squares minimizes the sum of squared errors.
- This is the same as maximizing the likelihood of the observed data if you 
  start thinking of the problem in terms of probabilities and probability 
  distribution functions
- This is sometimes called "maximum likelihood estimation"


#### More than one way to do it
- Gradient Descent is an alternate method to least squares.
- Basically iterates to find the line that best follows the contours defined 
  by the data.
- Can make sense when dealing with 3D data
- Easy to try in Python and just compare the results to least squares
  - But usually least squares is a perfect good choice.


#### Measuring error with r-squared
- How do we measure how well our line fits our data?
- R-squared (aka coefficient of determiantion) measures:
  - The fraction of the total variation of Y that is captured by the model

#### Computing r-squared
$$1.0 - \frac{sum of squared errors}{sum of squared variation from mean}$$

#### Interpreting r-squared
- Ranges from 0 to 1
- 0 is bad (none of the variance is captured)
- 1 is good (all of the variance is captured)

Refer to `linear.py` for coding exercises.


### Polynomial Regression

#### Why limit ourselves to straightlines?
- Not all relationships are linear.
- Linear formula: `y = mx + b`
  - This is a "first order" or "first degree" polynomial, as the power of x
    is 1
- Second order polynomial: `y = ax^2 + bx + c`
- Third order: `y = ax^3 + bx^2 + cx + d`
- Higher order produce more complex curves

#### Beware overfitting
- Don't use more degrees than you need
- Visualize your data first to see how complex a curve there might really be
- Visualize the fit - is your curve going out of its way to accomodate outliers?
- A high r-squared simply means your curve fits your $training data$ well;
  but it may not be a good predictor.
- Later we'll talk about more principled ways to detect overfitting (train/test)

Refer to `polynomial.py` for coding exercises.


### Multiple Regression, and Predicting Car Prices

#### Multiple Regression
- What if more than one variable influences the one you're interested in?
- Example: predicting a price for a car based on its many attributes (body
  style, brand, mileage, etc.)
- If you also have multiple dependent variables -- things you're trying to 
  predict -- that's "multivariate regression"

#### Still uses least squares
- We just end up with coefficients for each factor.
  - For example, $price = \alpha + \beta_1 mileage + \beter_2 age + \beta_3 doors$
  - These coefficients imply how important each factor is (if the data is all
    normalized!)
  - Get rid of ones that don't matter!
- Can still measure fit with r-squared
- Need to assume that the different factors are not themselves dependent on 
  each other.



### Multi-Level Models

- The concept is that some effects happen at various levels.
- Example: your health depends on a hierarchy of the health of your cells, organs,
  you as a whole, your family, your city, and the world you live in.
- Your wealth depends on your own work, what your parents did, what your grandparents
  did, etc.
- Multi-level models attempt to model and account for these interdependencies.

#### Modeling multiple levels
- You must identify the factors that affect the outcome you're trying to predict at 
  each level.
- For example - SAT scores might be predicted based on the genetics of individual
  children, the home environment of individual children, the crime rate of the 
  neighborhood they live in, the quality of the teachers in the school, the funding of 
  their school distrcit, and the ducation policies of their states.
- Some of these factors affect more than one level. FOr example, crime rate might
  influence the home environment too.

#### Doing this is hard
- Multi-level models showed up on some data science job requirements
- Entire advanced statistics and modeling courses exist on this one topic alone.
- "Modeling Multi-Level Systems", Octavian Iordache
