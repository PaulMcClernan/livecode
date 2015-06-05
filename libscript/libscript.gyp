{
	'includes':
	[
		'../common.gypi',
		'stdscript-sources.gypi',
	],
	
	'variables':
	{
		'libscript_public_headers':
		[
			'include/script.h',
			'include/script-auto.h',
		],
		
		'libscript_private_headers':
		[
			'src/script-private.h',
		],
		
		'libscript_sources':
		[
			'src/script-builder.cpp',
			'src/script-instance.cpp',
			'src/script-module.cpp',
			'src/script-object.cpp',
			'src/script-package.cpp',
		],
	},
	
	'targets':
	[
		{
			'target_name': 'libScript',
			'type': 'static_library',
			
			'toolsets': ['host','target'],
			
			'dependencies':
			[
				'../libfoundation/libfoundation.gyp:libFoundation',
				'../thirdparty/libffi/libffi.gyp:libffi',
			],
			
			'include_dirs':
			[
				'include',
				'src',
			],
			
			'sources':
			[
				'<@(libscript_public_headers)',
				'<@(libscript_private_headers)',
				'<@(libscript_sources)',
			],
			
			'direct_dependent_settings':
			{
				'include_dirs':
				[
					'include',
				],
			},
			
			'conditions':
			[
				[
					'OS == "linux" or OS == "android"',
					{
						'link_settings':
						{
							'libraries':
							[
								'-ldl',
							],
						},	
					},
				],
			],
		},
		{
			'target_name': 'stdscript',
			'type': 'static_library',
			
			'toolsets': ['host','target'],
			
			'dependencies':
			[
				'libScript',
				'../libfoundation/libfoundation.gyp:libFoundation',
			],
			
			'include_dirs':
			[
				'include',
				'src',
			],
			
			'sources':
			[
				'<@(stdscript_sources)',
			],
		},
	],
}
