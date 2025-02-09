function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);


for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
%    temp = zeros(size(theta));
%    h = transpose(theta) * transpose(X);
%    
%    for j = 1 : length(theta)
%      for i = 1 : m
%        temp(j) = temp(j) +  (h(i) - y(i)) * X(i,j);
%      end
%    end
%    theta(j) = theta(j) - (alpha) * (temp(j)/m);
    
    k=1:m;
      j1=(1/m)*sum((theta(1)+theta(2).*X(k,2))-y(k))
      j2=(1/m)*sum(((theta(1)+theta(2).*X(k,2))-y(k)).*X(k,2))
      theta(1)=theta(1)-alpha*(j1);
      theta(2)=theta(2)-alpha*(j2);
    



    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

  

end
