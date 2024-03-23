# install flask from pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.0.3', # or the appropriate version compatible with Flask 2.1.0
  provider => 'pip3',
}

