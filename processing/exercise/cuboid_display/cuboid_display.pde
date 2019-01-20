// by nodewee
// 2016/09
// https://nodewee.github.io

/*
=== Function Keys ===
[Mouse Move] change rotate degree
[Mouse Down] change background color
[g] gif record switch
*/

import gifAnimation.*;
import processing.opengl.*;

float xnoise = 0.0;
float ynoise = 0.0;
float inc = 0.05;
float xOffset = 0.0;
int gridY = 10;
int gridX = 10;
PGraphics pgmemo;
int memoY = 0;
int memoSize = 150;
String[] memo = new String[6];
float rotateDegree=0.5;

GifMaker gifExport;
boolean gifmaking=false;

float textZhigh=50;
float zoffset=50;

color bgcolor;


void setup() {
  size(600, 800, P3D);
  //fullScreen(P3D);
  strokeWeight(2);
  pgmemo = createGraphics(width, height);

  memo[0] = "ORDER";
  memo[1] = "CHAOS";
  memo[2]="";
  memo[3]="nodewee";
  memo[4]="";
  memo[5]="";

  gifExport = new GifMaker(this, "export.gif");
  gifExport.setRepeat(0); // make it an "endless" animation
  gifExport.setTransparent(255, 0, 0); // make black the transparent color. every black pixel in the animation will be transparent
}



void draw() {
  background(bgcolor);

  lights();
  
  pgmemo.beginDraw();
  pgmemo.textSize(memoSize);
  pgmemo.fill(255);
  pgmemo.background(0);
  for (int i=0; i<6; i++) {
    //text roll
    pgmemo.text(memo[i], (pgmemo.width-pgmemo.textWidth(memo[i]))/2, (pgmemo.height-memoY+i*memoSize));
    //text not roll
    //pgmemo.text(memo[i], (pgmemo.width-pgmemo.textWidth(memo[i]))/2, (pgmemo.height-height/1.5+i*memoSize));
  }
  pgmemo.endDraw();
  memoY=memoY+gridY;
  if (memoY>pgmemo.height*2) {
    memoY=0;
  }

  //translate(0, 0, -200);

  rotateDegree=map(mouseY, 0, height, 0, PI);
  rotateX(rotateDegree);
  rotateX(0.5);

  textZhigh=map(mouseX, 0, width, 0, 200);

  pgmemo.loadPixels();

  ynoise = 0.0;
  xnoise = xOffset;
noStroke();
  for (int x = 0; x < width; x+=gridX) {

    for (int y = 0; y <height; y+=gridY) {
      ynoise = ynoise + inc;
      float z=0;
      z = map(brightness(pgmemo.get(x, y)), 0, 255, 0, textZhigh); // z value of memo
      z = z+ map(noise(xnoise, ynoise), 0, 1, 0, 300); //z value of noise wave
      //z=z+zoffset; //z value of view setting

      pushMatrix();
      
      fill(150+map(z,0,150,0,105));
      translate(x, y, -200);
      box(gridX, gridY, z);
      popMatrix();
    }
    ynoise = 0.0;
    xnoise = xnoise + inc;
  }

  xOffset += inc/6.0;
  

  if (gifmaking) {
    gifExport.setDelay(1);
    gifExport.addFrame();
  }
}



void keyPressed() {
  if (key == CODED) {
    if (keyCode == UP) {
      rotateDegree+=0.01;
    } else if (keyCode == DOWN) {
      rotateDegree-=0.01;
    } else if (keyCode == LEFT) {
      zoffset-=10;
    } else if (keyCode == RIGHT) {
      zoffset+=10;
    }
  } else {
    if (key=='g'| key=='G') {
      gifmaking=!gifmaking;
      if (!gifmaking) {
        gifExport.finish();
        println("gif saved");
      } else {
        println("gif rec...");
      }
    }
  }
}

void mousePressed() {
  bgcolor=color(random(255), random(255), random(255));
}
