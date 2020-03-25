function J = computeCost(X, y, theta)

m = length(y);


J = 1/(2*m) * sum ((X*theta-y).^2);

end
