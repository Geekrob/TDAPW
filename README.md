# TDPW

TDPW(TDAP-QE) is an time dependent ab initio package, which is based on the plane-wave code *[Quantum Espresso](https://www.quantum-espresso.org/)*.

Chao Lian and Sheng Meng wrote the  original version. <br>
Now, it is mainly maintained by  Daqiang Chen, Chao Lian, and Sheng Meng.


## Publications
- [C. Lian, S.J. Zhang, S.Q. Hu, M.X. Guan, S. Meng*. Ultrafast charge ordering by self-amplied exciton-phonon dynamics in TiSe2. Nature Commun. 10, 43 (2020).](http://everest.iphy.ac.cn/papers/NComm11.43.pdf)


# Install this manual
## Install gem & bundle
## Install the dependencies with [Bundler](http://bundler.io/):
~~~bash
$ bundle install
~~~
The Gemfile in this dir is
```
source 'https://mirrors.tuna.tsinghua.edu.cn/rubygems'
#https://rubygems.org'

gem 'jekyll', '3.8.4'

group :jekyll_plugins do
  gem 'jekyll-feed', '0.11.0'
  gem 'jekyll-seo-tag', '2.5.0'
  gem 'jekyll-sitemap', '1.2.0'
end
```
## Run

Run `jekyll` commands through Bundler to ensure you're using the right versions:

~~~bash
nohup bundle exec jekyll serve -P 3000 > /tmp/outout.log
~~~