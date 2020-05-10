% read image
I = imread('chokeUnion.png');

%to binary
I = im2bw(I);

%to colored
I3(:,:,1)  = uint8(I) .* 255;
I3(:,:,2)  = uint8(I) .* 255;
I3(:,:,3)  = uint8(I) .* 255;

%show and save
imshow(I3)
imwrite(I3, 'unionNewFormat.png')