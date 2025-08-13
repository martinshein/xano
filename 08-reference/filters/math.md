---
category: filters
has_code_examples: false
last_updated: '2025-01-23'
tags:
- API
- Database
- Functions
- Queries
- Authentication
title: Math
---

# Math

[🛠️]The Visual Builder
    :::
        ::: 
            ::: 
            -   Swagger (OpenAPI Documentation)
            :::
            ::: 
            -   Async Functions
            :::
        -   Background Tasks
        -   Triggers
        -   Middleware
        -   Configuring Expressions
        -   Working with Data
        :::
        ::: 
        -   AI Tools
            ::: 
                ::: 
                -   External Filtering Examples
                :::
            -   Get Record
            -   Add Record
            -   Edit Record
            -   Add or Edit Record
            -   Patch Record
            -   Delete Record
            -   Bulk Operations
            -   Database Transaction
            -   External Database Query
            -   Direct Database Query
            -   Get Database Schema
            :::
            ::: 
            -   Create Variable
            -   Update Variable
            -   Conditional
            -   Switch
            -   Loops
            -   Math
            -   Arrays
            -   Objects
            -   Text
            :::
        -   Security
            ::: 
            -   Realtime Functions
            -   External API Request
            -   Lambda Functions
            :::
        -   Data Caching (Redis)
        -   Custom Functions
        -   Utility Functions
        -   File Storage
        -   Cloud Services
        :::
        ::: 
        -   Manipulation
        -   Math
        -   Timestamp
        -   Text
        -   Array
        -   Transform
        -   Conversion
        -   Comparison
        -   Security
        :::
        ::: 
        -   Text
        -   Expression
        -   Array
        -   Object
        -   Integer
        -   Decimal
        -   Boolean
        -   Timestamp
        -   Null
        :::
        ::: 
        -   Response Caching
        :::
-   ::: 
    Testing and Debugging
    :::
-   ::: 
    The Database
    :::
        ::: 
        -   Using the Xano Database
        -   Field Types
        -   Relationships
        -   Database Views
        -   Export and Sharing
        -   Data Sources
        :::
        ::: 
        -   Airtable to Xano
        -   Supabase to Xano
        -   CSV Import & Export
        :::
        ::: 
        -   Storage
        -   Indexing
        -   Maintenance
        -   Schema Versioning
        :::
-   ::: 
    Build For AI
    :::
        ::: 
        -   Templates
        :::
        ::: 
        -   Connecting Clients
        -   MCP Functions
        :::
-   ::: 
    Build With AI
    :::
-   ::: 
    File Storage
    :::
-   ::: 
    Realtime
    :::
-   ::: 
    Maintenance, Monitoring, and Logging
    :::
        ::: 
        :::
-   ::: 
    Building Backend Features
    :::
        ::: 
        -   Separating User Data
        -   Restricting Access (RBAC)
        -   OAuth (SSO)
        :::
-   ::: 
    Xano Features
    :::
        ::: 
        -   Release Track Preferences
        -   Static IP (Outgoing)
        -   Change Server Region
        -   Direct Database Connector
        -   Backup and Restore
        -   Security Policy
        :::
        ::: 
        -   Audit Logs
        :::
        ::: 
        -   Xano Link
        -   Developer API (Deprecated)
        :::
        ::: 
        -   Master Metadata API
        -   Tables and Schema
        -   Content
        -   Search
        -   File
        -   Request History
        -   Workspace Import and Export
        -   Token Scopes Reference
        :::
-   ::: 
    Xano Transform
    :::
-   ::: 
    Xano Actions
    :::
-   ::: 
    Team Collaboration
    :::
-   ::: 
    Agencies
    :::
        ::: 
        -   Agency Dashboard
        -   Client Invite
        -   Transfer Ownership
        -   Agency Profile
        -   Commission
        -   Private Marketplace
        :::
-   ::: 
    Custom Plans (Enterprise)
    :::
        ::: 
            ::: 
                ::: 
                -   Choosing a Model
                :::
            :::
        -   Tenant Center
        -   Compliance Center
        -   Security Policy
        -   Instance Activity
        -   Deployment
        -   RBAC (Role-based Access Control)
        -   Xano Link
        -   Resource Management
        :::
-   ::: 
    Your Xano Account
    :::
-   ::: 
    Troubleshooting & Support
    :::
        ::: 
        -   When a single workflow feels slow
        -   When everything feels slow
        -   RAM Usage
        -   Function Stack Performance
        :::
        ::: 
        -   Granting Access
        -   Community Code of Conduct
        -   Community Content Modification Policy
        -   Reporting Potential Bugs and Issues
        :::
-   ::: 
    Special Pricing
    :::
-   ::: 
    Security
    :::
-   ::: 
    :::
    abs
Was this helpful?
Copy
1.  [[🛠️]The Visual Builder](../building-with-visual-development.html)
2.  Filters
Math 
====
NOTE
When a filter below refers to the **parent value**, we\'re talking about the value box that lives immediately above the filter.
[]
<div>
</div>
abs
Returns the absolute value
The abs filter is useful when you need the magnitude of a value regardless of its sign. For example, when calculating distances between two points or finding the difference between two values without caring about direction.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The number to get the absolute value of
    :::
Input
Output
-5
5
10
10
-3.14
3.14
acos
Calculates the arc cosine of the supplied value in radians
The acos filter is useful when working with trigonometric calculations, such as determining angles in navigation systems, game development for character movement, or calculating positions in geometric applications.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A number between -1 and 1 representing a cosine value
    :::
Input
Output
1
0
0
1.5707963267948966
-1
3.141592653589793
acosh
Calculates the inverse hyperbolic cosine of the supplied value in radians
The acosh filter is useful in advanced mathematical modeling, such as in engineering calculations, physics simulations, or specialized scientific applications where hyperbolic functions are needed.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A number greater than or equal to 1
    :::
Input
Output
1
0
2
1.3169578969248166
10
2.993222846126381
add
Add 2 values together and return the answer
The add filter is useful for combining numeric values, such as calculating a total price from multiple items, combining measurements, or incrementing counters in your application.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first number in the addition
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second number to add to the primary value
    :::
Input
Output
5, 3
8
-2, 7
5
10.5, 4.2
14.7
array\_max
Returns the max of the values of the array
The array\_max filter is helpful when you need to find the highest value in a collection of numbers, such as determining the highest score, finding the maximum temperature in a data set, or identifying peak values in any numerical array.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An array of numbers
    :::
Input
Output
\[1, 5, 3, 9, 2\]
9
\[-10, -5, -20\]
-5
\[3.14, 2.71, 9.81\]
9.81
array\_min
Returns the min of the values of the array
The array\_min filter is valuable when you need to find the lowest value in a collection of numbers, such as determining the lowest price, finding the minimum temperature in a data set, or identifying the smallest entry in any numerical array.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An array of numbers
    :::
Input
Output
\[1, 5, 3, 9, 2\]
1
\[-10, -5, -20\]
-20
\[3.14, 2.71, 9.81\]
2.71
asin
Calculates the arc sine of the supplied value in radians
The asin filter is useful in trigonometric applications, such as calculating angles in physics simulations, determining trajectories in navigation, or solving geometric problems that involve angles.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A number between -1 and 1 representing a sine value
    :::
Input
Output
0
0
1
1.5707963267948966
-1
-1.5707963267948966
asinh
Calculates the inverse hyperbolic sine of the supplied value in radians
The asinh filter is useful in specialized mathematical applications, such as signal processing, electrical engineering calculations, or advanced scientific computations that require hyperbolic functions.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: Any number
    :::
Input
Output
0
0
1
0.8813735870195429
-2
-1.4436354751788103
atan
Calculates the arc tangent of the supplied value in radians
The atan filter is useful when determining angles from slopes or ratios, such as in computer graphics for calculating rotation angles, in robotics for sensor interpretation, or in navigation systems for heading calculations.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: Any number representing a tangent value
    :::
Input
Output
0
0
1
0.7853981633974483
-1
-0.7853981633974483
atanh
Calculates the inverse hyperbolic tangent of the supplied value in radians
The atanh filter is valuable in specialized fields like electrical engineering, signal processing, and certain physics applications where hyperbolic functions are required for modeling or calculations.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A number between -1 and 1 (exclusive)
    :::
Input
Output
0
0
0.5
0.5493061443340548
-0.75
-0.9729550745276566
avg
Returns the average of the values of the array
The avg filter is essential when you need to calculate the mean value of a set of numbers, such as finding the average score, determining average temperature over time, or calculating mean values in statistical analysis.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An array of numbers
    :::
Input
Output
\[1, 2, 3, 4, 5\]
3
\[10, 20, 30, 40\]
25
\[2.5, 3.5, 4.5\]
3.5
bitwise\_and
Bitwise AND 2 values together and return the answer
The bitwise\_and filter is useful in operations that require bit-level manipulation, such as flag checking in permissions systems, hardware control applications, or optimization in low-level programming where individual bits need to be examined.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first integer for the bitwise operation
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second integer to AND with the primary value
    :::
Input
Output
5, 3
1
12, 10
8
255, 15
15
bitwise\_or
Bitwise OR 2 values together and return the answer
The bitwise\_or filter is valuable when you need to combine bit flags, such as setting permissions in a security system, enabling features in configuration settings, or manipulating bitmap data where individual bits represent distinct options.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first integer for the bitwise operation
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second integer to OR with the primary value
    :::
Input
Output
5, 3
7
12, 10
14
240, 15
255
bitwise\_xor
Bitwise XOR 2 values together and return the answer
The bitwise\_xor filter is useful in cryptographic applications, error detection, toggling states, or finding differences between binary patterns, such as in data validation or simple encryption techniques.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first integer for the bitwise operation
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second integer to XOR with the primary value
    :::
Input
Output
5, 3
6
12, 10
6
255, 255
0
ceil
Round a decimal up to its integer equivalent
The ceil filter is helpful when you need to round a number up to the nearest integer, such as calculating the number of containers needed for items, determining the number of pages required for pagination, or rounding up financial values.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The number to round up
    :::
Input
Output
3.1
4
7.9
8
-2.3
-2
cos
Calculates the cosine of the supplied value in radians
The cos filter is essential in trigonometric calculations, such as determining coordinates in circular motion, calculating projections in physics, or modeling periodic phenomena like waves or oscillations.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An angle in radians
    :::
Input
Output
0
1
1.5707963267948966
0
3.141592653589793
-1
deg2rad
Convert degrees to radians
The deg2rad filter is useful when working with trigonometric functions that require radian inputs, such as converting user-friendly degree inputs to the radians needed for mathematical calculations in graphics, navigation, or physics simulations.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An angle in degrees
    :::
Input
Output
0
0
90
1.5707963267948966
180
3.141592653589793
divide
Divide 2 values together and return the answer
The divide filter is essential for calculations involving ratios, rates, or proportional values, such as determining per-unit costs, calculating percentages, or finding averages when the total and count are known separately.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The dividend (number being divided)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The divisor (number to divide by)
    :::
Input
Output
10, 2
5
9, 3
3
7, 2
3.5
exp
Returns the exponent of mathematical expression \"e\"
The exp filter is valuable in calculations involving growth or decay, such as compound interest, population growth models, radioactive decay, or any application where natural exponential growth is needed.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The exponent to which e is raised
    :::
Input
Output
0
1
1
2.718281828459045
2
7.3890560989306495
floor
Round a decimal down to its integer equivalent
The floor filter is useful when you need to round down to the nearest integer, such as truncating decimal places in financial calculations, determining complete units from fractional values, or implementing integer division behavior.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The number to round down
    :::
Input
Output
3.7
3
8.1
8
-2.3
-3
ln
Returns the natural logarithm
The ln filter is important in calculations involving exponential growth or decay, such as calculating compound interest over time, analyzing population growth, or solving equations where the unknown is in an exponent.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A positive number
    :::
Input
Output
1
0
2.718
0.9998141515394643
10
2.302585092994046
log
Returns the logarithm with a custom base
The log filter is valuable when working with logarithms in different bases, such as in information theory with base-2 logs, in chemistry with base-10 logs, or in custom scaling applications where a specific logarithmic base is required.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A positive number
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    base: The base of the logarithm (default is e)
    :::
Input
Output
100, 10
2
8, 2
3
81, 3
4
log10
Returns the Base-10 logarithm
The log10 filter is useful in applications where powers of 10 are significant, such as in the pH scale, decibel measurements, Richter scale for earthquakes, or any calculation where order of magnitude is important.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: A positive number
    :::
Input
Output
1
0
10
1
100
2
max
Returns the max both values
The max filter is helpful when you need to find the larger of two values, such as implementing upper bounds, determining the highest possible value between two options, or finding maximums in pairwise comparisons.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first number to compare
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second number to compare
    :::
Input
Output
5, 10
10
-3, -7
-3
8.2, 8.15
8.2
min
Returns the min both values
The min filter is useful when you need to find the smaller of two values, such as implementing lower bounds, determining the lowest possible value between two options, or finding minimums in pairwise comparisons.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first number to compare
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second number to compare
    :::
Input
Output
5, 10
5
-3, -7
-7
8.2, 8.15
8.15
modulus
Modulus 2 values together and return the answer
The modulus filter is valuable for calculating remainders after division, such as in cycling through arrays, implementing time formats (hours, minutes, seconds), creating patterns that repeat at regular intervals, or determining if a number is even or odd.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The dividend (number being divided)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The divisor (number to divide by)
    :::
Input
Output
7, 3
1
15, 4
3
-8, 3
-2
multiply
Multiply 2 values together and return the answer
The multiply filter is essential for scaling values, calculating areas, volumes, or any operation where a value needs to be repeated a certain number of times, such as determining total cost based on quantity and unit price.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The first factor in the multiplication
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The second factor to multiply by the primary value
    :::
Input
Output
4, 3
12
2.5, 6
15
-7, 2
-14
number\_format
Format a number with flexible support over decimal places, thousands separator, and decimal separator.
The number\_format filter is useful when displaying numerical data in user interfaces, financial reports, or any context where consistent formatting of numbers enhances readability, such as displaying prices, large statistics, or percentages.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The number to format
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    decimal\_places: Number of decimal places to display (default 0)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    decimal\_separator: Character to use as decimal point (default \".\")
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    thousands\_separator: Character to use as thousands separator (default \",\")
    :::
Input
Output
1234.56, 2, \".\", \",\"
1,234.56
1234.56, 0, \".\", \",\"
1,235
1234.56, 2, \",\", \" \"
1 234,56
pow
Returns the value raised to the power of exp.
The pow filter is valuable for exponential calculations, such as compound interest, geometric growth, area and volume calculations, or any mathematical operation involving powers.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The base number
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    exponent: The power to raise the base to
    :::
Input
Output
2, 3
8
10, 2
100
3, 0.5
1.7320508075
product
Returns the product of the values of the array
The product filter is useful when you need to multiply all values in a collection, such as calculating factorial values, determining compound growth across multiple periods, or finding the total area when given multiple dimensions.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An array of numbers
    :::
Input
Output
\[2, 3, 4\]
24
\[1.5, 2, 3\]
9
\[10, 0.1, 5\]
5
rad2deg
Convert radians to degrees
The rad2deg filter is helpful when converting from mathematical calculations (which typically use radians) to user-friendly degree displays, such as in navigation applications, angle measurements in user interfaces, or converting results from trigonometric functions.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An angle in radians
    :::
Input
Output
0
0
1.5707963267948966
90
3.141592653589793
180
round
Round a decimal with optional precision
The round filter is essential for formatting numerical values to a specific precision, such as financial calculations, scientific measurements, or any scenario where a specific number of decimal places is required.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The number to round
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    precision: Number of decimal places (default 0)
    :::
Input
Output
3.14159, 2
3.14
2.5, 0
3
-3.55, 1
-3.6
sin
Calculates the sine of the supplied value in radians
The sin filter is crucial in trigonometric applications, such as modeling wave patterns, calculating vertical components in physics, determining heights in triangulation, or generating smooth oscillatory motion in animations.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An angle in radians
    :::
Input
Output
0
0
1.5707963267948966
1
3.141592653589793
0
sqrt
Returns the square root of the value
The sqrt filter is valuable for calculations involving area-to-length conversions, calculating distances using the Pythagorean theorem, or normalizing values in statistical applications.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The non-negative number to calculate the square root of
    :::
Input
Output
4
2
9
3
2
1.4142136
subtract
Subtract 2 values together and return the answer
The subtract filter is useful for calculating differences, such as determining net change, finding remaining amounts after deductions, or calculating time intervals between events.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: The minuend (number being subtracted from)
    :::
-   ::: 
    ::: 
    :::
    :::
    ::: 
    value: The subtrahend (number to subtract)
    :::
Input
Output
10, 4
6
5, 8
-3
3.5, 1.2
2.3
sum
Returns the sum of the values of the array
The sum filter is essential when you need to add up all values in a collection, such as calculating total expenses, finding the sum of scores, or determining the total of any set of numerical values.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An array of numbers
    :::
Input
Output
\[1, 2, 3, 4, 5\]
15
\[-1, 0, 1\]
0
\[10.5, 20.3, 5.7\]
36.5
tan
Calculates the tangent of the supplied value in radians
The tan filter is important in trigonometric applications, such as calculating slopes, determining heights using angles and distances, or any application where the ratio of sine to cosine is needed.
Inputs:
-   ::: 
    ::: 
    :::
    :::
    ::: 
    primary value: An angle in radians
    :::
Input
Output
0
0
0.7853981633974483
1
3.141592653589793
0
Last updated 4 months ago
Was this helpful?