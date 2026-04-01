# py-logify

A lightweight and easy-to-use Python logging module inspired by a simplified Log4j-style API. \
It provides a flexible, simple interface for logging with minimal configuration.

## Usage

### Basic Setup

```python
import logify

# Create a logger instance
logger = logify.Logger("MyLogger")

# Add a standard output appender
standard_output_appender = logify.appenders.StandardOutput("stdout")

# Add a file appender
file_appender = logify.appenders.File("file", "logfile.log")

# Add appenders to the logger
logger.add_appender(standard_output_appender)
logger.add_appender(file_appender)

# Log a message
logger.info('This is an info message.')
logger.debug('This is a debug message.')
logger.error('This is an error message.')
```

### Custom Appender, Layout and Filter

Custom appenders, layouts, and filters can be created by subclassing the respective base classes.

## Contributing

Check out the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
