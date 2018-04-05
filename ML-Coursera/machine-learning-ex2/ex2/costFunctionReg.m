function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

%for j = 2 : length(grad)
%
%  h = sigmoid(transpose(theta) * transpose(X));
%
%  for i = 1 : length(X)
%    grad(1) = grad(1) + (h(i) - y(i)) * X(i,j);
%    grad(j) = grad(j)*(lambda) + (h(i) - y(i)) * X(i,j); 
%  end
%    grad(j) = grad(j) / m;
%end
h = sigmoid(transpose(theta) * transpose(X));

for i = 1 : length(X)
  J = J + (1/m) *( -y(i)*log(h(i)) - (1-y(i))*log(1-h(i)) );
  end
for j = 2 : length(theta)
  J = J + (lambda/(2*m)) * (theta(j)^2);    
  end


for j = 1 : length(grad)
  if (j = 1)
    lambda = 0
  for i = 1 : length(X)
    grad(j) = grad(j)*(lambda) + (h(i) - y(i)) * X(i,j);
    end  
  end
    grad(j) = grad(j) / m;
  
  h = sigmoid(transpose(theta) * transpose(X));
end






% =============================================================

end
