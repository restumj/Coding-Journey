// --------------------------------
// Pong Game by Restu Manujaya
// --------------------------------

#include "raylib.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct Circle {
    float x;
    float y;
    float rad;
    Color color;
} Circle;

typedef struct Player {
    int score;
} Player;

// Functions
int getRandomInRange(int min, int max) {
    return rand() % (max-min+1) + min;
}

// Player Info
Player leftPlayer = {0}, rightPlayer = {0};

int main(int argc, char const *argv[]) {
    InitWindow(800,600,"Pong by Restu Manujaya");
    SetTargetFPS(60);
    srand(time(NULL));

    // Initialitation for the pads
    Rectangle leftPad = {10,0,30,100};
    Rectangle rightPad = {GetScreenWidth()-40,0,30,100};

    // Initialization for the ball
    int selectedRange = rand() % 2;
    double angle;
    if (selectedRange == 0) {
        angle = (getRandomInRange(155,225));
    } else {
        int temp = getRandomInRange(-25,25);
        angle = 360-((temp<0) ? -temp:temp);
    }
    Vector2 v = {cos(DEG2RAD*angle),sin(DEG2RAD*angle)};
    Circle ball = {GetScreenWidth()/2,GetScreenHeight()/2,10,BLACK};
    unsigned int ballSpeed = 125;

    // Initialization for the score
    char scoreText[30];

    while (!WindowShouldClose()) {
        // Get the dt (Delta Time)
            float dt = GetFrameTime();

        // INPUT
            if (v.x != 0 && v.y != 0) {
                if (IsKeyDown(KEY_W)) leftPad.y -= dt*290;
                if (IsKeyDown(KEY_S)) leftPad.y += dt*290;
                if (IsKeyDown(KEY_UP)) rightPad.y -= dt*290;
                if (IsKeyDown(KEY_DOWN)) rightPad.y += dt*290;
            } else {
                if (IsKeyDown(KEY_W) || IsKeyDown(KEY_S) || IsKeyDown(KEY_UP) || IsKeyDown(KEY_DOWN)) {
                    ballSpeed = 125;
                    selectedRange = rand() % 2;
                    if (selectedRange == 0) {
                        angle = (getRandomInRange(155,225));
                    } else {
                        int temp = getRandomInRange(-25,25);
                        angle = 360-((temp<0) ? -temp:temp);
                    }
                    v.x = cos(DEG2RAD*angle);
                    v.y = sin(DEG2RAD*angle);
                }
            }
        
        // Logic (Ball Bouncing)
            // 1) Edge Vertical Screen
            if ((ball.y-ball.rad) <= 0 || (ball.y+ball.rad) >= GetScreenHeight()) {
                v.y *= -1;
            }
            // 2) Left Pad
            else if ((ball.x-ball.rad) <= leftPad.x+leftPad.width && ball.y >= leftPad.y && ball.y <= leftPad.y+leftPad.height) {
                v.x *= -1;
                ballSpeed += 25;
            }
            // 3) Right Pad
            else if ((ball.x+ball.rad) >= rightPad.x && ball.y >= rightPad.y && ball.y <= rightPad.y+rightPad.height) {
                v.x *= -1;
                ballSpeed += 25;
            }

        // Scoring
            if (ball.x-ball.rad <= 0) {
                rightPlayer.score += 1;
                v.x=0;
                v.y=0;
                ball.x = GetScreenWidth()/2;
                ball.y = GetScreenHeight()/2;
            } else if (ball.x+ball.rad>=GetScreenWidth()) {
                leftPlayer.score += 1;
                v.x=0;
                v.y=0;
                ball.x = GetScreenWidth()/2;
                ball.y = GetScreenHeight()/2;
            }

        // Restrict the pad movement
            // Left Pad
            if (leftPad.y <= 0) {
                leftPad.y = 0;
            } else if (leftPad.y+leftPad.height >= GetScreenHeight()) {
                leftPad.y = GetScreenHeight()-leftPad.height;
            }
            // Right Pad
            if (rightPad.y <= 0) {
                rightPad.y = 0;
            } else if (rightPad.y+rightPad.height >= GetScreenHeight()) {
                rightPad.y = GetScreenHeight()-rightPad.height;
            }

        BeginDrawing();
            ClearBackground(RAYWHITE);
            
            // Draw Left Pad
            DrawRectangleRounded(leftPad,0.1f,0,BLACK);
            // Draw Right Pad
            DrawRectangleRounded(rightPad,0.1f,0,BLACK);
            // Draw the Ball
            ball.x += v.x*ballSpeed*dt;
            ball.y += v.y*ballSpeed*dt;
            DrawCircle(ball.x,ball.y,ball.rad,ball.color);

            // Draw the Score
            snprintf(scoreText,sizeof(scoreText),"%d : %d", leftPlayer.score, rightPlayer.score);
            auto int scoreTextWidth = MeasureText(scoreText,30);
            DrawText(scoreText,(GetScreenWidth()/2)-(scoreTextWidth/2),20,30,ORANGE);
        EndDrawing();
    }
    
    CloseWindow();
    return 0;

}