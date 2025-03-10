import ArrayAndHashing from "../src/ArraysAndHashing";
import {describe, expect, it} from '@jest/globals';

describe('Testing Array and Hashing problems', () => {
    it('should test Two Sum problem', () => {
        const arrayAndHashing = new ArrayAndHashing();
        const twoSum = arrayAndHashing.twoSum;

        expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
        expect(twoSum([3, 2, 4], 6)).toEqual([1, 2]);
        expect(twoSum([3, 3], 6)).toEqual([0, 1]);
        expect(twoSum([3, 2, 4], 7)).toEqual([0, 2]);
        expect(twoSum([2, 7, 11, 15], 10)).toEqual([]);
        expect(twoSum([3, 3], 7)).toEqual([]);
    });

    it('shouls test Contains Duplicate problem', () => {
        const arrayAndHashing = new ArrayAndHashing();
        const containsDuplicate = arrayAndHashing.containsDuplicate;
        
        expect(containsDuplicate([1, 2, 3, 1])).toBe(true);
        expect(containsDuplicate([1, 2, 3, 4])).toBe(false);
        expect(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).toBe(true);

        const containsDuplicateAlternative = arrayAndHashing.containsDuplicateAlternative;

        expect(containsDuplicateAlternative([1, 2, 3, 1])).toBe(true);
        expect(containsDuplicateAlternative([1, 2, 3, 4])).toBe(false);
        expect(containsDuplicateAlternative([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).toBe(true);
    });
});