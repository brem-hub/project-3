from objects.number import Number
from objects.complex import Complex
from objects.fraction import Fraction
from objects.polar import Polar


number_types = {
    Number.TYPE.COMPLEX: Complex,
    Number.TYPE.FRACTION: Fraction,
    Number.TYPE.POLAR: Polar
}
