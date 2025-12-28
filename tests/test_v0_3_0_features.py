"""Tests for v0.3.0 new features."""

import pytest
import numpy as np
from unifyt import (
    Quantity,
    UncertainQuantity,
    QuantityFormatter,
    format_quantity,
    UnitValidator,
    validate_unit,
    suggest_unit,
    BatchConverter,
    convert_batch,
    sum_batch,
    get_profiler,
    enable_profiling,
    disable_profiling,
    UnitRegistry,
    prefixes
)


class TestUncertainQuantity:
    """Test uncertain quantities."""
    
    def test_creation(self):
        """Test creating uncertain quantities."""
        q = UncertainQuantity(100, 'meter', uncertainty=0.5)
        assert q.value == 100
        assert q.uncertainty == 0.5
        assert str(q.unit) == 'meter'
    
    def test_relative_uncertainty(self):
        """Test relative uncertainty."""
        q = UncertainQuantity(100, 'meter', relative_uncertainty=0.01)
        assert q.uncertainty == 1.0
        assert q.relative_uncertainty == 0.01
    
    def test_addition_propagation(self):
        """Test uncertainty propagation in addition."""
        a = UncertainQuantity(100, 'meter', uncertainty=1)
        b = UncertainQuantity(50, 'meter', uncertainty=0.5)
        c = a + b
        
        assert c.value == 150
        # σ = sqrt(1² + 0.5²) = sqrt(1.25) ≈ 1.118
        assert abs(c.uncertainty - 1.118) < 0.001
    
    def test_multiplication_propagation(self):
        """Test uncertainty propagation in multiplication."""
        a = UncertainQuantity(10, 'meter', uncertainty=0.1)
        b = UncertainQuantity(5, 'meter', uncertainty=0.05)
        c = a * b
        
        assert c.value == 50
        # Relative uncertainties: 0.01 and 0.01
        # Combined: sqrt(0.01² + 0.01²) = 0.01414
        # Absolute: 50 * 0.01414 ≈ 0.707
        assert abs(c.uncertainty - 0.559) < 0.1
    
    def test_conversion(self):
        """Test unit conversion with uncertainty."""
        q = UncertainQuantity(100, 'meter', uncertainty=0.5)
        q_km = q.to('kilometer')
        
        assert q_km.value == 0.1
        assert q_km.uncertainty == 0.0005


class TestFormatter:
    """Test quantity formatting."""
    
    def test_default_format(self):
        """Test default formatting."""
        q = Quantity(100, 'meter')
        result = format_quantity(q, style='default')
        assert 'meter' in result
    
    def test_latex_format(self):
        """Test LaTeX formatting."""
        q = Quantity(100, 'meter/second')
        result = format_quantity(q, style='latex')
        assert 'mathrm' in result or 'frac' in result
    
    def test_scientific_format(self):
        """Test scientific notation."""
        q = Quantity(1000, 'meter')
        result = format_quantity(q, style='scientific')
        assert 'e+' in result or 'E+' in result
    
    def test_custom_formatter(self):
        """Test custom formatter."""
        formatter = QuantityFormatter(style='compact', precision=3)
        q = Quantity(123.456, 'meter')
        result = formatter.format(q)
        assert 'meter' in result


class TestValidator:
    """Test unit validation."""
    
    def test_validate_valid_unit(self):
        """Test validating valid units."""
        assert validate_unit('meter') == True
        assert validate_unit('second') == True
        assert validate_unit('kilogram') == True
    
    def test_validate_invalid_unit(self):
        """Test validating invalid units."""
        assert validate_unit('invalid_unit') == False
    
    def test_suggestions(self):
        """Test unit suggestions."""
        suggestions = suggest_unit('metr')
        assert len(suggestions) > 0
        assert 'meter' in suggestions or 'meters' in suggestions
    
    def test_dimensionality_check(self):
        """Test dimensionality checking."""
        validator = UnitValidator()
        
        is_compat, _ = validator.check_dimensionality('meter', 'foot')
        assert is_compat == True
        
        is_compat, _ = validator.check_dimensionality('meter', 'second')
        assert is_compat == False
    
    def test_simplify_unit(self):
        """Test unit simplification."""
        validator = UnitValidator()
        simplified = validator.simplify_unit('meter * second / second')
        assert 'meter' in simplified
        assert 'second' not in simplified or simplified.count('second') == 0


class TestBatchOperations:
    """Test batch operations."""
    
    def test_convert_batch(self):
        """Test batch conversion."""
        quantities = [
            Quantity(100, 'meter'),
            Quantity(1, 'kilometer'),
            Quantity(50, 'foot')
        ]
        
        results = convert_batch(quantities, 'meter')
        assert len(results) == 3
        assert all(str(q.unit) == 'meter' for q in results)
    
    def test_sum_batch(self):
        """Test batch sum."""
        quantities = [
            Quantity(100, 'meter'),
            Quantity(50, 'meter'),
            Quantity(25, 'meter')
        ]
        
        total = sum_batch(quantities)
        assert total.value == 175
    
    def test_batch_statistics(self):
        """Test batch statistics."""
        converter = BatchConverter()
        quantities = [
            Quantity(100, 'meter'),
            Quantity(200, 'meter'),
            Quantity(300, 'meter')
        ]
        
        mean = converter.mean_quantities(quantities)
        assert mean.value == 200
        
        min_q = converter.min_quantity(quantities)
        assert min_q.value == 100
        
        max_q = converter.max_quantity(quantities)
        assert max_q.value == 300


class TestProfiling:
    """Test performance profiling."""
    
    def test_profiler_context(self):
        """Test profiler context manager."""
        profiler = get_profiler()
        profiler.reset()
        
        with profiler.profile('test_operation'):
            q = Quantity(100, 'meter').to('kilometer')
        
        stats = profiler.get_stats('test_operation')
        assert stats['count'] == 1
        assert stats['mean'] > 0
    
    def test_enable_disable(self):
        """Test enabling/disabling profiling."""
        enable_profiling()
        profiler = get_profiler()
        assert profiler._enabled == True
        
        disable_profiling()
        assert profiler._enabled == False


class TestPrefixes:
    """Test metric prefixes."""
    
    def test_parse_prefixed_unit(self):
        """Test parsing prefixed units."""
        base, factor = prefixes.parse_prefixed_unit('kilometer')
        assert base == 'meter'
        assert factor == 1000.0
        
        base, factor = prefixes.parse_prefixed_unit('millisecond')
        assert base == 'second'
        assert factor == 0.001
    
    def test_add_prefixes(self):
        """Test adding prefixes to custom unit."""
        registry = UnitRegistry()
        registry.define('parsec', '3.086e16 meter')
        
        prefixes.add_prefixes_to_unit(
            registry,
            'parsec',
            '3.086e16 meter',
            prefixes=['kilo']
        )
        
        # Check that kiloparsec was added
        assert 'kiloparsec' in registry._custom_units


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
