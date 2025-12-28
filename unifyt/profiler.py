"""Performance profiling utilities for Unifyt operations."""

import time
import functools
from typing import Callable, Any, Dict, List
from collections import defaultdict
import numpy as np


class PerformanceProfiler:
    """
    Performance profiler for tracking operation times.
    
    Examples:
        >>> profiler = PerformanceProfiler()
        >>> with profiler.profile('conversion'):
        ...     q = Quantity(100, 'meter').to('kilometer')
        >>> profiler.print_stats()
    """
    
    def __init__(self):
        """Initialize profiler."""
        self._timings: Dict[str, List[float]] = defaultdict(list)
        self._enabled = True
    
    def enable(self):
        """Enable profiling."""
        self._enabled = True
    
    def disable(self):
        """Disable profiling."""
        self._enabled = False
    
    def profile(self, operation_name: str):
        """
        Context manager for profiling an operation.
        
        Args:
            operation_name: Name of the operation being profiled
        
        Examples:
            >>> profiler = PerformanceProfiler()
            >>> with profiler.profile('my_operation'):
            ...     # code to profile
            ...     pass
        """
        return ProfileContext(self, operation_name)
    
    def record_time(self, operation_name: str, duration: float):
        """
        Record timing for an operation.
        
        Args:
            operation_name: Name of the operation
            duration: Duration in seconds
        """
        if self._enabled:
            self._timings[operation_name].append(duration)
    
    def get_stats(self, operation_name: str = None) -> Dict[str, Any]:
        """
        Get statistics for operations.
        
        Args:
            operation_name: Specific operation (None for all)
        
        Returns:
            Dictionary of statistics
        
        Examples:
            >>> profiler = PerformanceProfiler()
            >>> stats = profiler.get_stats('conversion')
            >>> print(stats['mean'])
        """
        if operation_name:
            if operation_name not in self._timings:
                return {}
            
            times = self._timings[operation_name]
            return self._calculate_stats(times)
        else:
            return {
                name: self._calculate_stats(times)
                for name, times in self._timings.items()
            }
    
    def _calculate_stats(self, times: List[float]) -> Dict[str, float]:
        """Calculate statistics for a list of times."""
        if not times:
            return {}
        
        times_array = np.array(times)
        return {
            'count': len(times),
            'total': float(np.sum(times_array)),
            'mean': float(np.mean(times_array)),
            'std': float(np.std(times_array)),
            'min': float(np.min(times_array)),
            'max': float(np.max(times_array)),
            'median': float(np.median(times_array)),
        }
    
    def print_stats(self, operation_name: str = None):
        """
        Print profiling statistics.
        
        Args:
            operation_name: Specific operation (None for all)
        """
        stats = self.get_stats(operation_name)
        
        if operation_name:
            if not stats:
                print(f"No profiling data for '{operation_name}'")
                return
            
            print(f"\nProfiling stats for '{operation_name}':")
            self._print_operation_stats(stats)
        else:
            print("\nProfiling Statistics:")
            print("=" * 60)
            for name, op_stats in stats.items():
                print(f"\n{name}:")
                self._print_operation_stats(op_stats)
    
    def _print_operation_stats(self, stats: Dict[str, float]):
        """Print statistics for a single operation."""
        print(f"  Count:  {stats['count']}")
        print(f"  Total:  {stats['total']*1000:.3f} ms")
        print(f"  Mean:   {stats['mean']*1000:.3f} ms")
        print(f"  Std:    {stats['std']*1000:.3f} ms")
        print(f"  Min:    {stats['min']*1000:.3f} ms")
        print(f"  Max:    {stats['max']*1000:.3f} ms")
        print(f"  Median: {stats['median']*1000:.3f} ms")
    
    def reset(self, operation_name: str = None):
        """
        Reset profiling data.
        
        Args:
            operation_name: Specific operation (None for all)
        """
        if operation_name:
            if operation_name in self._timings:
                del self._timings[operation_name]
        else:
            self._timings.clear()
    
    def export_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Export all statistics as a dictionary.
        
        Returns:
            Dictionary of {operation_name: stats}
        """
        return self.get_stats()


class ProfileContext:
    """Context manager for profiling."""
    
    def __init__(self, profiler: PerformanceProfiler, operation_name: str):
        """Initialize context."""
        self.profiler = profiler
        self.operation_name = operation_name
        self.start_time = None
    
    def __enter__(self):
        """Enter context."""
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context."""
        duration = time.perf_counter() - self.start_time
        self.profiler.record_time(self.operation_name, duration)


def profile_function(operation_name: str = None):
    """
    Decorator for profiling functions.
    
    Args:
        operation_name: Name for the operation (default: function name)
    
    Examples:
        >>> @profile_function('my_func')
        ... def my_function():
        ...     pass
    """
    def decorator(func: Callable) -> Callable:
        name = operation_name or func.__name__
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            
            # Store in global profiler if available
            if hasattr(wrapper, '_profiler'):
                wrapper._profiler.record_time(name, duration)
            
            return result
        
        return wrapper
    
    return decorator


# Global profiler instance
_global_profiler = PerformanceProfiler()


def get_profiler() -> PerformanceProfiler:
    """
    Get the global profiler instance.
    
    Returns:
        Global PerformanceProfiler instance
    
    Examples:
        >>> profiler = get_profiler()
        >>> profiler.print_stats()
    """
    return _global_profiler


def enable_profiling():
    """Enable global profiling."""
    _global_profiler.enable()


def disable_profiling():
    """Disable global profiling."""
    _global_profiler.disable()


def print_profiling_stats():
    """Print global profiling statistics."""
    _global_profiler.print_stats()


def reset_profiling():
    """Reset global profiling data."""
    _global_profiler.reset()
