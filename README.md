# A Python Flask APM agent shim

[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)

# Overview
This project is a Flask shim for an C++ based APM agent.  It will preprocess both the request and response side of a REST API exchange, and create various telemetry about the exchange.  This data will be stored in a CSV file, but that will be extended pretty quickly.

# Dependencies
| Dependency              | Version | URL                                         |
|-------------------------|---------|---------------------------------------------|
| CMake                   | 3.8     | https://github.com/Kitware/CMake            |
| Google Protocol Buffers | 3.7.1   | https://github.com/protocolbuffers/protobuf |
| Google Test             | 1.8.1   | https://github.com/google/googletest        |

For more detail on dependencies you can always refer to the .travis.yml for Dockerfiles.

# Summary
I cannot reveal the company this challenge is for - they ask that their name not be used lest other candidates find a submitted solution and draw inspiration from it (if not outright plagiarize it).

However the conditions of this challenge are pretty cool.  The code remains the property of the applicant and they encourage it's inclusion into the applicant's portfolio... even to use to it present to other prospective employers!

This is pretty progressive thinking.  It stands in stark contrast to some other parasitic creatures at unethical organizations that essentially are using code challenges as a source of free labor.

I encourage you to check it out and see if it has anything to offer you.  It is released under the GPLv3.  The Flask extension under the simplified BSD license.

