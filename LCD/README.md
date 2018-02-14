# Code for LCD

## How it works:
- Heart rate is converted into a string and printed on screen (updated every x ms)
- Heart animation:
    - Heart image is saved on flash mem as a sprite
    - To animate it, we define an array that decribes the sprite's velocity at each point in time
    - Update the position of the heart sprite with the current timeframe's velocity
    - Loop through the animation

## TODO:
- Position and resize the heart rate and heart animation
- Change animation values to look good
- Figure out what update rate to use for updating the heart rate 
(right now it's every 1s)
- Figure out how we're getting the heart rate from the main 
micro-controller
- Make sure the sprite & text don't interfere