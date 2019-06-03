import java.util.*;

public class Main{
  public static void main(String[] args) {
    int Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;
    Scanner sc = new Scanner(System.in);
    int[] points = new int[8];
    for(int i=0; i<8; i++) {
      points[i] = sc.nextInt();
    }
    Point Astart = new Point(points[0], points[1]);
    Point Aend = new Point(points[2], points[3]);
    Point Bstart = new Point(points[4], points[5]);
    Point Bend = new Point(points[6], points[7]);

    Point Avector = distract(Aend, Astart);
    Point Bvector = distract(Bend, Bstart);

    float s1 = 0;
    float s2 = 1;
    float new_s1, new_s2;

    for (int i=0; i<50; i++) {
      float l = (s2-s1) / 3;
      new_s1 = s1 + l;
      new_s2 = s1 + 2*l;

      Point A1 = plus(Astart, Avector.multiply(new_s1));
      Point A2 = plus(Astart, Avector.multiply(new_s2));
      Point B1 = plus(Bstart, Bvector.multiply(new_s1));
      Point B2 = plus(Bstart, Bvector.multiply(new_s2));

      if (getDistance(A1,B1) < getDistance(A2,B2)) {
        s2 = new_s2;
      }
      else {
        s1 = new_s1;
      }
      if (i == 49) {
        System.out.println(getDistance(A1,B1));
      }
    }
  }

  public static double getDistance(Point A, Point B) {
    return Math.sqrt(Math.pow(B.x - A.x, 2) + Math.pow(B.y - A.y, 2));
  }

  public static Point distract(Point A, Point B) {
    return new Point(A.x - B.x, A.y - B.y);
  }

  public static Point plus(Point A, Point B) {
    return new Point(A.x + B.x, A.y + B.y);
  }
}

class Point {
  double x;
  double y;
  public Point(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public Point multiply(float n) {
    return new Point(this.x * n, this.y * n);
  }
}
