Binary Star Simulation

The simulation is done using python and solving the two-body system (which is why i have considered the distance from the centre of mass for the two stars, and their distance as well.), and modifying the Keplers laws a bit to visualize the gravitational interactions between the two stars.

To simulate the gravity between the two stars,  the stars are put to the longitudinal extremum and latitudinally at the middle.
The Newton's second law of motion has been used in its very basic sense, F= ma, where the accelaeration is the second derivative of the distance, and with each unit of time passing by, the differential equation is solved (which may be very evident looking at the code)

Thus, at start, vectorially the velocity along x for both the stars is zero while the velocity along y is due to the centrifugal force calculated using the two body dynamics and gravity.

The rest of the calculation are followed in the code.