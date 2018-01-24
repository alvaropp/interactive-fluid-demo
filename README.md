# interactive-fluid-twitter

An implementation of [interactive-fluid-demo](https://github.com/ngcm/interactive-fluid-demo) which runs on a server monitoring a given Twitter account. Whenever a tweet is written mentioning that Twitter account and attaching an image, the software will instantly grab the image, run the fluid flow simulation on top of that image and tweet an animated GIF back.

Can be easily run on any Linux box, just follow the [instructions](https://github.com/ngcm/interactive-fluid-demo#installation). Moreover, we provide [Vagrant](https://www.vagrantup.com/) recipe to create a virtual machine with all the necessary software installed. This is very convenient as it can be quickly deployed somewhere to run non-stop.

![example1](https://user-images.githubusercontent.com/4785303/35059288-8757857c-fbb2-11e7-9b96-b0d32f02744f.gif)
![example2](https://user-images.githubusercontent.com/4785303/35060001-eb033510-fbb4-11e7-8d14-384632987b6b.gif)
