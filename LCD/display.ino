/**
 * This program is based off of code from: https://github.com/lexus2k/ssd1306
 *
 *
 *   Attiny85 PINS
 *             ____
 *   RESET   -|_|  |- 3V
 *   SCL (3) -|    |- (2)
 *   SDA (4) -|    |- (1)
 *   GND     -|____|- (0)
 *
 *   Atmega328 PINS: connect LCD to A4/A5
 */

#include "ssd1306.h"
#include "sprite_pool.h"
#include "font6x8.h"

/* 
 * Heart image below is defined directly in flash memory.
 * This reduces SRAM consumption.
 * The image is defined from bottom to top (bits), from left to
 * right (bytes).
 */
const PROGMEM uint8_t heartImage[8] =
{
    0B00001110,
    0B00011111,
    0B00111111,
    0B01111110,
    0B01111110,
    0B00111101,
    0B00011001,
    0B00001110
};

/*
 * Define sprite width. The width can be of any size.
 * But sprite height is always assumed to be 8 pixels
 * (number of bits in single byte).
 */
const int spriteWidth = sizeof(heartImage);

/* Declare sprite pool object here                            *
 * Sprite pool is responsible for update LCD's areas, touched *
 * by sprites. By default, it clears area under the sprite -  *
 * see SpritePool::drawBlock() library method. But you may    *
 * override that method, and draw anything you need for the   *
 * block, defined by column and row.                          */
SpritePool s_pool;


/* Declare variable that represents our sprite */
SPRITE sprite;
int speedY = 1;


void setup()
{
    /* Do not init Wire library for Attiny controllers */
    ssd1306_128x64_i2c_init();
    ssd1306_fillScreen(0x00);


    /* Set range of the SpritePool field on the screen in blocks. *
     * Use whole LCD display                                      *
     * 0,0   means left-top block of lcd display.                 *
     *                         that is 0*8=0 - pixel              *
     *                                 0*8=0 - pixel              *
     * 15,7  means right-bottom block of lcd:                     *
     *                         that is 15*8+7=127-th pixel        *
     *                                 7*8+7=63-rd pixel          */
    s_pool.setRect( (SSD1306_RECT) { 0, 0, 15, 7 } );


    /* Create sprite at 32,8 position in pixels. The function initializes sprite structure. */
    // SPRITE ssd1306_createSprite(uint8_t x, uint8_t y, uint8_t w, const uint8_t *data);
    sprite = ssd1306_createSprite( 32, 8, spriteWidth, heartImage );


    /* Add created sprite to the sprite pool.                     *
     * Sprite pool doesn't store sprites themselve, only pointers,*
     * so, do not use local variables for the sprites.            */
    s_pool.add( sprite );



    ssd1306_fillScreen(0x00);
    ssd1306_setFixedFont(ssd1306xled_font6x8);
    // Print the heart rate
    const char ch[] = {"..."}; // Temp text
    // uint8_t ssd1306_printFixedN(uint8_t xpos, uint8_t y, const char ch[], EFontStyle style, uint8_t factor);
    ssd1306_printFixedN(8, 16, "...", STYLE_NORMAL, 2); // 4x font size


    /* Redraw whole LCD-display */
    s_pool.refreshScreen();
}


void updateHeartRate(int hr) {
    /** Updates the global heart rate string with a new heart rate. */
    char text[] = "   ";

    if ((hr > 0) && (hr < 10)) {
        text[2] = hr + 48; // Ascii value of digit
        text[1] = " ";
        text[0] = " ";
    }
    else if ((hr >= 10) && (hr < 100)) {
        text[2] = (hr % 10) + 48; // Ones
        text[1] = (hr / 10) + 48; // Tens
        text[0] = " ";            // Hundreds
    }
    else if ((hr >= 100) && (hr < 1000)) {
        text[2] = (hr % 10) + 48;         // Ones
        text[1] = ((hr % 100) / 10) + 48; // Tens
        text[0] = (hr / 100) + 48;        // Hundreds
    }
    else {
        /** Should never get here (maybe blink screen or print on screen to show errors?) */
    }
}


CONST int heart_bounce_animation[] = {
         1, 1, 2, 3, 5, 7, 5, 3, 2, 1, 1, 
        -1,-1,-2,-3,-5,-7,-5,-3,-2,-1,-1, 
}
int animation_frame = 0;
char current_heart_rate_text[4] = "   ";
void loop()
{
    /** TODO:
            - Position and resize the heart rate and heart animation
            - Change animation values to look good
            - Figure out what update rate to use for updating the heart rate 
            (right now it's every 1s)
            - Figure out how we're getting the heart rate from the main 
            micro-controller
            - Make sure the sprite & text don't interfere
    */
    delay(100);


    /** Heart bouncing animation, want to do smooth bouncing.
        To make this simple, we store the change in Y at every time step in an
        array, this will have the `bounce` effect instead of just simply moving
        up and down.
        Move sprite every 100 milliseconds. The animation takes 2s.
    */

    /* Do the heart bounce animation */
    sprite.y += speedY * heart_bounce_animation[animation_frame];


    /* Only update the text at certain intervals */
    if ((animation_frame % 10) == 0) {
        /* Update heart rate text! */
        updateHeartRate(80 + count/10); // The value in here should be read into the one of the pins
        ssd1306_printFixedN(8, 16, current_heart_rate_text, STYLE_NORMAL, 2);

        /* Redraw whole LCD-display */
        s_pool.refreshScreen();
    }
    else {
        /* Redraw only those areas, affected by sprites */
        s_pool.drawSprites();
    }

    
    /* Move to next element in the animation */
    animation_frame++;
    if (animation_frame == 20) animation_frame = 0;
}




