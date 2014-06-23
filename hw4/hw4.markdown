## Week 4 Assignment

### Problem 1. Trigonometric functions.

Create a simple plot that displays the sin(x) and cos(x) functions from x = -Pi to x = Pi. Use different colors for the two plots, which should be plotted in one figure. The plots should be properly labeled. Submit your plot via Moodle as a `FirstName-LastName-trig.pdf` file for both instructor and peer assessment.

- Use `numpy.linspace()` to create an array of floats between `-numpy.pi` and `numpy.pi`.
- Use `numpy.sin()` and `numpy.cos()` functions on the arrays.
- Always label you axes. Your figure should have a descriptive title as well as your first and last name.

### Problem 2. Income Versus Age.

Using the Illinois census data `ss12pil.csv`, make a scatter plot of the age versus income of all respondents older than 18 and annual income in excess of $1000. Submit your plot via Moodle as a `FirstName-LastName-income_age.pdf` file for both instructor and peer assessment. Here are some hints:

- The column header for age is "AGEP".
- The column header for income is "PINCP".
- Persons less than 15 years old have no income values (blank fields).
- By now, you should know several ways to extract the columns you want from a file. To give you a few examples, you could use `awk` to extract the columns and save it in a separate file; you could write a simple loop generate lists in Python; or you could use `numpy.loadtxt()` and numpy arrays. Choose your favorite method.
- Always label your axes. Your figure should have a descriptive title as well as your first and last name.

### Problem 3. Age distribution of males and females.

Using the Illinois census data `ss12pil.csv`, create a plot that displays multiple histograms for the age distribution of males and females. You should use different colors for the two histograms, which should be plotted side-by-side (like the last histogram in the iPython notebook), and the two histograms should be properly labeled. Submit your plot via Moodle as a `FirstName-LastName-age_dist.pdf` file for both instructor and peer assessment.

- The column header for sex is "SEX".
- 1 in the "SEX" column corresponds to male; 2 female.
- Always label your axes. Your figure should have a descriptive title as well as your first and last name.
