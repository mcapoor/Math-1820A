clear; 
clc; 

%S2
[x,y,z]=sphere;
X = x;
Y = y;
Z = z + 1;
surf(X, Y, Z, FaceColor="none"); hold on

%R2
%[RX, RY] = meshgrid(-10:0.5:10,-10:0.5:10);
%surf(RX, RY, 0*RX); hold on

%Projection 
stereograph(0, 0, "red")

stereograph(0, pi/4, "blue")
stereograph(pi/2, pi/4, "green")
stereograph(pi/4, pi/2, "magenta")
stereograph(pi/3, pi/3, "cyan")

%Plotting
xlim([-5 5]);
ylim([-5 5]);
zlim([0 5]);

%Helper functions
function stereograph(theta, phi, color)
    N = cartesian(0, 0);

    p = cartesian(theta, phi);
    p_proj = project(p);

    plt(p, color)
    plt(p_proj, color)

    plt_line(N, p_proj, color)
end

function projected = project(p)
    projected = [-2*p(1)/(p(3) - 2) -2*p(2)/(p(3) - 2) 0];
end

function plt_line(p1, p2, color) 
    pts = [p1; p2];
    plot3(pts(:,1), pts(:,2), pts(:,3), 'LineStyle', '--', 'Color', color)
end

function plt(p, color)
    scatter3(p(1), p(2), p(3), 200, color, '.')
end

function P = cartesian(theta, phi) 
    x = sin(phi)*cos(theta);
    y = sin(phi)*sin(theta);
    z = cos(phi)+1;
    P = [x, y, z];
end