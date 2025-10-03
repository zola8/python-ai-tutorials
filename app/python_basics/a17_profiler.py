import cProfile
import pstats
import io


class SimpleProfiler:
    """A simple class that demonstrates profiling specific code blocks"""

    def __init__(self):
        self.profiler = None

    def profile_function(self, func, *args, **kwargs):
        """Profile a specific function call"""
        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)

        profiler.disable()

        # Print results
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s)
        ps.sort_stats('cumulative')
        ps.print_stats(5)  # Top 5 functions
        print(s.getvalue())

        return result

    def expensive_calculation(self, n):
        """An example expensive function"""
        total = 0
        for i in range(n):
            for j in range(n):
                total += i * j
        return total


# Usage example
if __name__ == "__main__":
    profiler = SimpleProfiler()

    # Profile the expensive calculation
    result = profiler.profile_function(profiler.expensive_calculation, 10000)
    print(f"Result: {result}")
